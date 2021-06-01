import pandas as pd
import random
import const

'''
I didn't have much time to create a repo and worry about naming. 
Instead, I just wrote rough time estimates of when I finished each steps.
I would have normally also written docs exmplaining what you would be getting back.
'''
class TemperatureStation:

    def __init__(self, csv_string):

        self.df = pd.read_csv(csv_string)

    # Learning pandas and got this about 10:45
    def getStationAndDateOfReportedLowestTemperature(self):

        all_lowest_temps = self.df[self.df[const.TEMPERATURE] == self.df[const.TEMPERATURE].min()]
        single_entry = all_lowest_temps.iloc[random.randint(0, len(all_lowest_temps)-1 )]

        return (single_entry[0], single_entry[1])

    # Finished step 2 around 11:30
    def getStationWithMostFluctuation(self, df=None):

        if df is None:
            df = self.df

        result_station = -1
        highest_fluctuation = -1

        # Get all data ponts per stations
        station_by_group = df.groupby(const.STATION_ID)

        # From there, calculate each stations total fluctations (+= per change from last)
        # Then keep the max of those compared to other stations.
        # If stations has a higher overall fluctiation, then keep that station_id
        for station in station_by_group:

            curr_fluctuation = self._getTotalFluctuation(station[1][const.TEMPERATURE])
            if curr_fluctuation > highest_fluctuation:
                highest_fluctuation = curr_fluctuation
                result_station = station[1].iloc[0][const.STATION_ID]

        return result_station
        
    def _getTotalFluctuation(self, station_temps):

        total_fluctuation = 0
        last_temp = None

        for temperature in station_temps:
            
            if last_temp is None:
                last_temp = temperature
            else:
                total_fluctuation += abs(last_temp - temperature)
                last_temp = temperature

        return total_fluctuation


    # 12:00 I still want to make some tests, however if you only want 2 hours mark this is it.
    def getStationWithMostFluctuataionsDateRange(self, date_start, date_end):

        # Create a new Dataframe where we only have dates from start to end
        date_range_df = self.df[(self.df[const.DATE] >= date_start) & (self.df[const.DATE] <= date_end)]
        return self.getStationWithMostFluctuation(date_range_df)



# Started around 10am I think
def main():
    temp_class = TemperatureStation("test.csv")
    print(temp_class.getStationAndDateOfReportedLowestTemperature())
    print(temp_class.getStationWithMostFluctuation())
    print(temp_class.getStationWithMostFluctuataionsDateRange(2000.375, 2000.710))

    
main()

