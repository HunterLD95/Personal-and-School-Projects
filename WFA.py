import pandas as pd
import datetime as dt
from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta

def Walk_Forward_Analysis_data(Data, Walking_Iteration, Training_end_year, Begin_Train_Month, Begin_Train_Day, Training_Years, Testing_Sets, Iteration, Train_Test_Results):
    """Walk Forward Analysis (WFA)
    This Function is used to break up data into date specific in sample and out of sample sets.
    These train and test sets can then be used later for the cross validation of a machine learning trading strategy.
Args:
    Data: Data must be a Pandas Dataframe with the date column already parsed.
    Walking Iteration: Current choices are monthly and weekly. This will be the size of the test set.
    Training End Year: This the year you would like the training set to stop.
    Begin Train Month: This will be the month you want the training set to stop. You must select 1-12.
    Begin Train Day: This will be the day you want the training set to stop. You must select 1-31, depending on the month of course.
    Training Years: This is the amount of years you would like the training set to be.
    Testing sets: This parameter is only applied to testing sets. This will be the number of testing sets created.
    Iteration Selection: This parameter must be a lower number than the amount of testing sets. It will be the testing set you select to show.
    Train Test Result: This is either Training or Testing, in terms of which sample you want to return.
Returns:
    pd.DataFrame: New dataframe of the train or test set.
"""
    Begin_Train_Year=Training_end_year-Training_Years
    if Walking_Iteration in ('Monthly','MTH','1M'):
        if Train_Test_Results in ('Train','Training','train','training'):
            # When selecting the iteration, 1 represents the first training or test set
            # Training Sets
            Training_results = []
            for i in range(12*Training_Years):
                Initial_Training_date = dt.datetime(Begin_Train_Year, Begin_Train_Month, Begin_Train_Day) + relativedelta(months=+i)
                Training_End = dt.datetime((Begin_Train_Year+Training_Years), Begin_Train_Month, Begin_Train_Day) + relativedelta(months=+i)
                TrainingSet = Data.loc[Initial_Training_date:Training_End]
                TrainingSet = TrainingSet.dropna()
                #Training_rets = expected_returns.returns_from_prices(TrainingSet) -- un-comment for Returns
                Training_results.append(pd.DataFrame(TrainingSet))
            return Training_results[Iteration-1]
        elif Train_Test_Results in ('Test','Testing','test','testing'):
            # Testing Sets
            Testing_results = []
            for x in range(Testing_Sets):
                Initial_Testing_date = dt.datetime((Begin_Train_Year+Training_Years), Begin_Train_Month, Begin_Train_Day) + relativedelta(months=+x)
                Testing_End = dt.datetime((Begin_Train_Year+Training_Years), (Begin_Train_Month+1), Begin_Train_Day) + relativedelta(months=+x)
                TestingSet = Data.loc[Initial_Testing_date:Testing_End]
                TestingSet = TestingSet.dropna()
                #Testing_rets = expected_returns.returns_from_prices(TestingSet)
                Testing_results.append(pd.DataFrame(TestingSet))
            return Testing_results[Iteration-1]
        elif Train_Test_Results not in ('Train','train','Training','training','Test','test','Testing','testing'):
            print('WARNING!!! Improper use of Training or Testing results Selection. Allowed Entries: Train, train, Training, training, Test, test, Testing, testing')
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------\
    # ---------------------------- Weekly Walk Forward Analysis-----------------------------------------------------------------------------------------------------------\
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------\
    elif Walking_Iteration in ('Weekly','1 Week','1W'):
        if Train_Test_Results in ('Train','Training','train','training'):
            # When selecting the iteration, 1 represents the first training or test set
            # Training Sets
            Training_results = []
            for i in range(52*Training_Years):
                Initial_Training_date = dt.datetime(Begin_Train_Year, Begin_Train_Month, Begin_Train_Day) + relativedelta(weeks=+i)
                Training_End = dt.datetime((Begin_Train_Year+Training_Years), Begin_Train_Month, Begin_Train_Day) + relativedelta(weeks=+i)
                TrainingSet = Data.loc[Initial_Training_date:Training_End]
                TrainingSet = TrainingSet.dropna()
                #Training_rets = expected_returns.returns_from_prices(TrainingSet)
                Training_results.append(pd.DataFrame(TrainingSet))
            return Training_results[Iteration-1]
        elif Train_Test_Results in ('Test','Testing','test','testing'):
            # Testing Sets
            Testing_results = []
            for x in range(Testing_Sets):
                Initial_Testing_date = dt.datetime((Begin_Train_Year+Training_Years), Begin_Train_Month, Begin_Train_Day) + relativedelta(weeks=+x)
                Testing_End = dt.datetime((Begin_Train_Year+Training_Years), Begin_Train_Month, (Begin_Train_Day+7)) + relativedelta(weeks=+x)
                TestingSet = Data.loc[Initial_Testing_date:Testing_End]
                TestingSet = TestingSet.dropna()
                #Testing_rets = expected_returns.returns_from_prices(TestingSet)
                Testing_results.append(pd.DataFrame(TestingSet))
            return Testing_results[Iteration-1]
        elif Train_Test_Results not in ('Train','train','Training','training','Test','test','Testing','testing'):
            print('WARNING!!! Improper use of Training or Testing results Selection. Allowed Entries: Train, train, Training, training, Test, test, Testing, testing')