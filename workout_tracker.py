class WorkoutTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout, duration_str):
        if not workout or not duration_str:
            return False, "Please enter both workout and duration."
        try:
            duration = int(duration_str)
            if duration <= 0:
                return False, "Duration must be a positive number."
            self.workouts.append({"workout": workout, "duration": duration})
            return True, f"'{workout}' added successfully!"
        except ValueError:
            return False, "Duration must be a number."

    def get_workout_list_text(self):
        if not self.workouts:
            return "No workouts logged yet."
        return "Logged Workouts:\n" + "\n".join(
            f"{i+1}. {w['workout']} - {w['duration']} minutes" for i, w in enumerate(self.workouts)
        )
