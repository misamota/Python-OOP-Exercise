def weekday_name(day_of_week):
    """Return name of weekday.
        
        if day_of_week in days:
            return days[day_of_week]
        else:
            return none

        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {1 : "Sunday",
            2: "Monday",
            3:"Tuesday",
            4: "Wednesday",
            5:"Thursday",
            6:"Friday",
            7:"Saturday"}
    if day_of_week in days:
        print(days[day_of_week])
        return days[day_of_week]
    else:
        print("invalid number")
        return None

weekday_name(1)
weekday_name(7)
weekday_name(9)
weekday_name(0)
