import streamlit as st


def add_time(start, duration, day=''):
    week_days = 'sunday monday tuesday wednesday thursday friday saturday'.split()

    # Getting the Start minutes
    start_minutes = int(start.split()[0].split(':')[0]) * 60 + int(start.split()[0].split(':')[1])
    if start.split()[1] == 'PM' and int(start.split()[0].split(':')[0]) != 12:
        start_minutes += 720

    # Getting Duration minutes
    dur_minutes = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    # Output Minutes
    out_minutes = dur_minutes + start_minutes

    # Conversion to hour:min
    hour, min = out_minutes // 60 % 24, out_minutes % 60
    # Getting AM and PM
    ender = 'AM' if hour < 12 else 'PM'

    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12

    # result_time
    result_time = f'{hour}:{min} {ender}'
    if min < 10:
        result_time = f'{hour}:0{min} {ender}'  # prepends a 0 to a single digit

    # handling days
    out_day = ''
    n = out_minutes // 60 // 24
    for i in range(7):
        if week_days[i] == day.lower():
            out_day = week_days[(i + n) % 7].capitalize()

    if day.lower() not in week_days:
        if n == 0:
            return result_time
        elif n == 1:
            return f'{result_time} (next day)'
        elif n > 1:
            return f'{result_time} ({n} days later)'

    else:
        if n == 0:
            return f'{result_time}, {out_day}'
        elif n == 1:
            return f'{result_time}, {out_day} (next day)'
        elif n > 1:
            return f'{result_time}, {out_day} ({n} days later)'


# Streamlit App
def main():
    st.title("Time Calculator")
    st.header("Add Time to a Start Time")

    # Input fields
    start_time = st.text_input("Enter the start time (e.g., '3:06 PM'):")
    duration_time = st.text_input("Enter the duration (e.g., '2:41'):")
    start_day = st.text_input("Enter the start day (optional, e.g., 'Monday'):")

    # Calculate button
    if st.button("Calculate"):
        if start_time and duration_time:
            try:
                result = add_time(start_time, duration_time, start_day)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please provide both a start time and a duration.")


if __name__ == "__main__":
    main()
