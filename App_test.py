import unittest
from ACEest_Fitness import WorkoutTracker


class TestWorkoutTracker(unittest.TestCase):
    def setUp(self):
        """Set up a new WorkoutTracker for each test."""
        self.tracker = WorkoutTracker()

    def test_add_workout_success(self):
        """Test successful addition of a workout."""
        success, message = self.tracker.add_workout("Pushups", "30")
        self.assertTrue(success)
        self.assertEqual(message, "'Pushups' added successfully!")
        self.assertEqual(len(self.tracker.workouts), 1)
        self.assertEqual(self.tracker.workouts[0]["workout"], "Pushups")
        self.assertEqual(self.tracker.workouts[0]["duration"], 30)

    def test_add_workout_invalid_duration(self):
        """Test adding a workout with a non-numeric duration."""
        success, message = self.tracker.add_workout("Pushups", "abc")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a number.")
        self.assertEqual(len(self.tracker.workouts), 0)

    def test_add_workout_zero_duration(self):
        """Test adding a workout with zero duration."""
        success, message = self.tracker.add_workout("Stretching", "0")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a positive number.")
        self.assertEqual(len(self.tracker.workouts), 0)

    def test_add_workout_negative_duration(self):
        """Test adding a workout with a negative duration."""
        success, message = self.tracker.add_workout("Time Travel", "-10")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a positive number.")
        self.assertEqual(len(self.tracker.workouts), 0)

    def test_view_workouts_empty(self):
        """Test viewing an empty workout list."""
        self.assertEqual(
            self.tracker.get_workout_list_text(), "No workouts logged yet."
        )

    def test_view_workouts_with_entries(self):
        """Test viewing a list with multiple workouts."""
        self.tracker.add_workout("Pushups", "30")
        self.tracker.add_workout("Squats", "20")
        expected = "Logged Workouts:\n1. Pushups - 30 minutes\n2. Squats - 20 minutes\n"
        self.assertEqual(self.tracker.get_workout_list_text(), expected)


if __name__ == "__main__":
    unittest.main()
