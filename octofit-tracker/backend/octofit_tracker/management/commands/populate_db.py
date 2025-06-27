from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create_user(username='alice', email='alice@example.com', password='password1')
        user2 = User.objects.create_user(username='bob', email='bob@example.com', password='password2')
        user3 = User.objects.create_user(username='carol', email='carol@example.com', password='password3')

        # Create teams
        team1 = Team.objects.create(name='Team Octopus')
        team2 = Team.objects.create(name='Team Dolphin')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Create workouts
        workout1 = Workout.objects.create(name='Morning Run', description='Run 2 miles', activity_type='running')
        workout2 = Workout.objects.create(name='Pushups', description='Do 20 pushups', activity_type='strength')
        workout3 = Workout.objects.create(name='Yoga', description='15 min yoga session', activity_type='flexibility')

        # Create activities
        Activity.objects.create(user=user1, activity_type='running', duration=30, points=10)
        Activity.objects.create(user=user2, activity_type='strength', duration=20, points=8)
        Activity.objects.create(user=user3, activity_type='flexibility', duration=15, points=6)

        # Create leaderboard
        Leaderboard.objects.create(team=team1, total_points=18, week=timezone.now().date())
        Leaderboard.objects.create(team=team2, total_points=6, week=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
