import datetime
import pandas as pd
import pygal
from IPython.display import display
from IPython.core.display import HTML


class Record(pd.DataFrame):

    def __init__(self, nutrition):
        super().__init__(nutrition)
        self.__record = nutrition

    def add(self, date, protein, carbon, fat):
        calorie = protein*4 + carbon*4 + fat*9
        new_record = pd.Series(
            {"Date": date, "Calorie": calorie, "Protein": protein, "Carbon": carbon, "Fat": fat})
        if self.__record[self.__record["Date"] == date].empty:
            new_data = self.__record.append(new_record, ignore_index=True)
        else:
            print("There has already been a record of the same date, please modify the record istead of adding a new one.")
            return Record(self.__record)
        return Record(new_data)

    def remove(self, date):

        record_to_remove = self.__record[self.__record["Date"] == date]
        if record_to_remove.empty:
            print("The record does NOT exist!")
            return Record(self.__record)
        else:
            print("Are you sure you want to delete the following record?\n",
                  record_to_remove)

        while True:
            check = input("""[1] for "YES"\n[2] for "NO and quit"\nChoice:""")
            if check == "1":
                break
            elif check == "2":
                return Record(self.__record)
            else:
                print("Invalid input, please re-enter.")
                continue

        new_data = self.__record[~(self.__record["Date"] == date)]
        return Record(new_data)

    def modify(self, date, protein, carbon, fat):

        row_to_modify = self.__record[self.__record["Date"] == date]
        if row_to_modify.empty:
            print("The record does NOT exist! Please check and try again!")
            return Record(self.__record)
        else:
            print("The record you are going to change:\n", row_to_modify)

        while True:
            check = input(
                "[1] for YES\n[2] for NO and return to the previous menu\nChoice:")
            if check == "1":
                break
            elif check == "2" or check == "q":
                return Record(self.__record)
            else:
                print("Invalid input, please re-enter.")
                continue

        if protein != '':
            self.__record.loc[row_to_modify.index[0], ("Protein",)] = protein
        if carbon != '':
            self.__record.loc[row_to_modify.index[0], ("Carbon",)] = carbon
        if fat != '':
            self.__record.loc[row_to_modify.index[0], ("Fat",)] = fat
        self.__record.loc[row_to_modify.index[0], ("Calorie",)] = self.__record.loc[row_to_modify.index[0], (
            "Protein",)]*4 + self.__record.loc[row_to_modify.index[0], ("Carbon",)]*4 + self.__record.loc[row_to_modify.index[0], ("Fat",)]*9
        new_data = self.__record
        return Record(new_data)

    def show(self, start_date, end_date, indicator=1):

        condition = (self.__record["Date"] >= start_date) & (
            self.__record["Date"] <= end_date)
        row_to_display = self.__record[condition]
        if row_to_display.empty:
            return "There is NO record between the selected dates."

        # indicator == 1 means the user wants to display the record of Calories
        if indicator == 1:
            graph = pygal.Bar()
            graph.title = "Calorie Consumption Between {} and {}".format(
                start_date, end_date)
            graph.add("Calorie", row_to_display["Calorie"])
            graph.x_labels = row_to_display["Date"]

        # indicator != 1 means the user wants to display the record of other nutritions
        else:
            # pie chart will be used to display the nutritions of a single day
            if len(row_to_display) == 1:
                graph = pygal.Pie()
                graph.title = "Nutrition Consumption On {} (in g)".format(
                    row_to_display["Date"].values[0])
                graph.add("Protein", row_to_display["Protein"].values[0])
                graph.add("Carbon", row_to_display["Carbon"].values[0])
                graph.add("Fat", row_to_display["Fat"].values[0])

            # stackedline will be used to display the nutritions of multiple days
            else:
                graph = pygal.StackedLine(fill=True)
                graph.title = "Nutrition Consumption From {} to {} (in g)".format(
                    start_date, end_date)
                for each in row_to_display.keys()[2:]:
                    graph.add(each, row_to_display[each].to_list())
                graph.x_labels = row_to_display["Date"].to_list()

        # display the graph
        graph_svg = graph.render(is_unicode=True)
        display(HTML(graph_svg))
