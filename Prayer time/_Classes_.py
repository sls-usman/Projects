import pandas


class PrayerTiming:
    data_frame = pandas.read_csv('LatLon.csv')
    list_of_states = []
    latitude = 0
    longitude = 0

    def __int__(self):
        self.logicals()

    def logicals(self):
        for key, value in PrayerTiming.data_frame.iterrows():
            PrayerTiming.list_of_states.append(value.states)

        for key, value in PrayerTiming.data_frame.iterrows():
            try:
                if 'sokoto' in PrayerTiming.list_of_states:
                    chosen_state = value
                    PrayerTiming.latitude = chosen_state.latitude
                    PrayerTiming.longitude = chosen_state.longitude

            except ValueError:
                print("here error")


PrayerTiming().logicals()
