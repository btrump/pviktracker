[ ] install bootstrap3 into templates, use inheritance

- Models:
	- Racer
		- first_name
		- lane_name
		- Handle
	- Heat
		- day (date)
		- number (int)
	- Lap
		- fk_racer
		- fk_heat
		- number
		- time
		