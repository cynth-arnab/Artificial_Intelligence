#hierarchicalplanner
class HierarchicalPlanner:
    def __init__(self):
        pass

    def plan_high_level_task(self, high_level_task):
        print(f"Planning high-level task: {high_level_task}")
        plan = []

        if high_level_task == "Plan a Trip":
            plan.extend(self.plan_subtask("Choose Destination"))
            plan.extend(self.plan_subtask("Book Transportation"))
            plan.extend(self.plan_subtask("Book Accommodation"))
            plan.extend(self.plan_subtask("Plan Itinerary"))

        return plan

    def plan_subtask(self, subtask):
        print(f"Planning subtask: {subtask}")
        plan = []

        if subtask == "Choose Destination":
            plan.extend(["Research Destinations", "Select Destination"])

        elif subtask == "Book Transportation":
            plan.extend(["Compare Flights", "Book Flights"])

        elif subtask == "Book Accommodation":
            plan.extend(["Search Hotels", "Book Hotel"])

        elif subtask == "Plan Itinerary":
            plan.extend(["List Attractions", "Plan Daily Activities"])

        return plan

    def execute_plan(self, plan):
        print("\nExecuting Plan:")
        for action in plan:
            print(f"Executing: {action}")

if __name__ == "__main__":
    hierarchical_planner = HierarchicalPlanner()
    high_level_task = "Plan a Trip"
    full_plan = hierarchical_planner.plan_high_level_task(high_level_task)
    hierarchical_planner.execute_plan(full_plan)
