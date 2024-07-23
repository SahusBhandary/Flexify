class Workout:
    def __init__ (self, workoutName, exercises):
        self.workoutName = workoutName
        self.exercises = exercises
    
    def getWorkoutName(self):
        return self.workoutName
    
    def getExercises(self):
        return self.exercises
    
    def setWorkoutName(self, newName):
        self.workoutName = newName