from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=25)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=30)

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1, user2])

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-01')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-02')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
