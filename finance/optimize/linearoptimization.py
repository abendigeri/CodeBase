import pulp

from optimize.models import Investment

# Instantiate our problem class


def getInvestments(total_amount, data):
    # print(data['constraints'])

    commitments = data['constraints']['commitments']

    average_return = data['constraints']['average_return']

    exclusions = data['constraints']['exclusions']

    db_objects = Investment.objects.all()

    model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)

    lp_variables = [pulp.LpVariable(
        i.name, lowBound=0, cat='Integer') for i in db_objects]

    # print(lp_variables)

    # Generating Objective Function

    # model += 9 * X1 + 12 * X2 + 15 * X3 + 8 * X4 + 6 * X5 + 3 * Xs, "Profit"
    x = 0
    for idx, i in enumerate(lp_variables):
        x += i * db_objects[idx].returns
    # print(x)

    model += x, "Profit"
    # print(model)

    # Adding the Constraints

    # 1) Constraint for the Total Sum

    x = 0
    for idx, i in enumerate(lp_variables):
        x += i

    model += x <= total_amount

    # 2) Average Risk Constraint
    x = 0
    for idx, i in enumerate(lp_variables):

        if db_objects[idx].risk > 0:
            x += db_objects[idx].risk * i - average_return * i

    model += x <= 0

    # print(x)

    # 3) Commitments

    x = 0
    for idx, i in enumerate(lp_variables):
        print(str(i))
        if str(i) == "CommercialLoans":
            x += (1 - 0.2) * i
        else:
            x += -0.2 * i

    model += x >= 0

    # print(x)

    # 3) Conditions

    model += lp_variables[5] + lp_variables[3] - lp_variables[1] <= 0

    # Solving the Model
    model.solve()

    pulp.LpStatus[model.status]

    for idx, i in enumerate(lp_variables):
        print(str(i)+" = {}".format(i.varValue))

    print(pulp.value(model.objective))

    pass


# X1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
# X2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
# X3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')
# X4 = pulp.LpVariable('x4', lowBound=0, cat='Integer')
# X5 = pulp.LpVariable('x5', lowBound=0, cat='Integer')
# Xs = pulp.LpVariable('xs', lowBound=0, cat='Integer')

# # Objective function
# model += 9 * X1 + 12 * X2 + 15 * X3 + 8 * X4 + 6 * X5 + 3 * Xs, "Profit"

# model += lp_variables[0]

# model += X1 + X2 + X3 + X4 + X5 + Xs <= 1000000000

# model += -2 * X1 + X2 + 3 * X3 - 3 * X4 - 4 * X5 <= 0

# model += -0.2* X1 - 0.2* X2 - 0.2 * X3 + 0.8 * X4 - 0.2 * X5 >= 0

# model += X2 + X3 - X1 <= 0

# model.solve()

# pulp.LpStatus[model.status]

# # Print our decision variable values
# print("X1 = {}".format(X1.varValue))
# print("X2 = {}".format(X2.varValue))
# print("X3 = {}".format(X3.varValue))
# print("X4 = {}".format(X4.varValue))
# print("X5 = {}".format(X5.varValue))
# print("Xs = {}".format(Xs.varValue))

# print(pulp.value(model.objective))
