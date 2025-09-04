import unittest
from workout_tracker import WorkoutTracker

class TestWorkoutTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = WorkoutTracker()

    def test_add_workout_success(self):
        success, message = self.tracker.add_workout("Pushups", "30")
        self.assertTrue(success)
        self.assertEqual(message, "'Pushups' added successfully!")
        self.assertEqual(len(self.tracker.workouts), 1)

    def test_add_workout_invalid_duration(self):
        success, message = self.tracker.add_workout("Pushups", "abc")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a number.")

    def test_add_workout_zero_duration(self):
        success, message = self.tracker.add_workout("Stretching", "0")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a positive number.")

    def test_add_workout_negative_duration(self):
        success, message = self.tracker.add_workout("Time Travel", "-10")
        self.assertFalse(success)
        self.assertEqual(message, "Duration must be a positive number.")

    def test_view_workouts_empty(self):
        self.assertEqual(self.tracker.get_workout_list_text(), "No workouts logged yet.")

    def test_view_workouts_with_entries(self):
        self.tracker.add_workout("Pushups", "30")
        self.tracker.add_workout("Squats", "20")
        expected = "Logged Workouts:\n1. Pushups - 30 minutes\n2. Squats - 20 minutes"
        self.assertEqual(self.tracker.get_workout_list_text(), expected)

if __name__ == "__main__":
    unittest.main()
