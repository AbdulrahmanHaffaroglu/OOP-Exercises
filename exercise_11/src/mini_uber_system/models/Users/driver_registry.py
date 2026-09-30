class DriverRegistry:
    drivers = {}
    id_num = 1


    @classmethod
    def register_driver(cls, driver):
        id = f"driver-{cls.id_num:03d}"
        cls.drivers[id] = driver
        cls.id_num += 1
        return id


    @classmethod
    def find_available(cls, vehicle_type):
        for driver in cls.drivers.values():
            if driver.status == "Available" and driver.vehicle_type == vehicle_type:
                return driver
            
        return None