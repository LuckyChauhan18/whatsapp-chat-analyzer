import pandas as pd
import re
def preprocess(data):
    # Define the pattern to extract dates and time
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    # Split the data into messages and dates
    messages = re.split(pattern, data)[1:]  # Skipping the first empty string caused by splitting
    dates = re.findall(pattern, data)

    # Ensure both lists have the same length
    if len(messages) != len(dates):
        raise ValueError(f"Mismatch in lengths: messages ({len(messages)}) and dates ({len(dates)})")

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert 'message_date' to datetime with error handling
    df['message_date'] = pd.to_datetime(df['message_date'], errors='coerce', format='%m/%d/%y, %H:%M - ')

    # Rename the column for clarity
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Extract users and messages from user_message column
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)  # Use raw string to avoid escape issues
        if entry[1:]:  # If there's a user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    # Add user and message columns to the DataFrame
    df['user'] = users
    df['message'] = messages

    # Drop the old user_message column
    df.drop(columns=['user_message'], inplace=True)

    # Extract various date-related features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Calculate the period based on hour
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append(f"00-{hour + 1}")
        else:
            period.append(f"{hour}-{hour + 1}")

    df['period'] = period

    return df