#Inductive Logic Programming
class Fact:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value


class Rule:
    def __init__(self, decision, conditions):
        self.decision = decision
        self.conditions = conditions


class LogicSystem:
    def __init__(self):
        self.facts = {}
        self.rules = []


    def add_fact(self, fact):
        attribute = fact.attribute
        self.facts.setdefault(attribute, []).append(fact)


    def add_rule(self, rule):
        self.rules.append(rule)


    def query(self, decision):

        for rule in self.rules:
            if self.match_rule(rule, decision):
                return rule.decision
        return "No decision made."


    def match_rule(self, rule, decision):

        return rule.decision == decision and all(self.has_fact(condition) for condition in rule.conditions)


    def has_fact(self, condition):

        return condition.attribute in self.facts and any(other_fact.attribute == condition.attribute and other_fact.value == condition.value for other_fact in self.facts[condition.attribute])


system = LogicSystem()


system.add_fact(Fact("student", "Alice"))
system.add_fact(Fact("difficulty", "High"))
system.add_fact(Fact("time_available", "Low"))
system.add_fact(Fact("preferred_learning_style", "Visual"))


rule1 = Rule("Study", [Fact("student", "Alice"), Fact("difficulty", "High"), Fact("time_available", "Low")])
rule2 = Rule("Study", [Fact("student", "Alice"), Fact("preferred_learning_style", "Visual")])
rule3 = Rule("Relax", [Fact("student", "Alice"), Fact("difficulty", "Low"), Fact("time_available", "High")])


system.add_rule(rule1)
system.add_rule(rule2)
system.add_rule(rule3)



decision = "No decision made."
if system.query("Study") == "Study":
    decision = "The logic system suggests studying."
elif system.query("Relax") == "Relax":
    decision = "The logic system suggests relaxing."


print(decision)
