# Notification System

This project implements a small notification system inspired by the exercise description in [src/notification_system/main.py](src/notification_system/main.py).

## Project Goal

The application should be able to send messages to users through different channels without depending on the specific channel type. The system supports:

- Email notifications
- SMS notifications
- Push notifications

The design is based on the idea that a user has a set of communication channels, and a notification can be sent using the same workflow regardless of the target channel.

## Main Concepts

### User
A `User` owns:

- personal data such as name, email, phone number, password, and device ID
- a list of placed orders
- a channel list for email, SMS, and push notifications

The `User` class provides methods such as:

- `place_order(order)`
- `cancel_order(order)`
- `pay_order(order)`
- `send_email(message, user)`
- `send_message(message, user)`
- `change_password(new_password)`

### Channel
The abstract base class `Channel` defines the contract for all notification channels. Each concrete channel implements `send(message, user=None)`.

### Notification
`Notification` represents a message being sent through one or more channels. It stores:

- the list of channels
- the message text
- the target user (if provided)

It then calls each channel's `send()` method with the message and user.

## Requirements Covered by the Code

This project follows the exercise requirements:

- notifications can be sent without knowing the concrete channel type
- each channel can send a message
- new channels can be added with minimal changes
- notifications include recipient information
- invalid actions such as duplicate orders or reusing the same password are handled with exceptions

## Project Structure

```text
exercise_8/
├── pyproject.toml
├── README.md
├── src/
│   └── notification_system/
│       ├── __init__.py
│       ├── main.py
│       └── models/
│           ├── __init__.py
│           ├── channel.py
│           ├── email.py
│           ├── notification.py
│           ├── push_notification.py
│           ├── sms.py
│           └── user.py
└── tests/
    ├── channel_test.py
    ├── email_test.py
    ├── sms_test.py
    ├── push_notification_test.py
    ├── notification_test.py
    └── user_test.py
```

## Running the Project

From the project root:

```bash
PYTHONPATH=src python -m notification_system.main
```

## Running the Tests

From the project root:

```bash
python -m pytest -q
```

## Testing Focus

The test suite checks the behavior expected from the exercise, including:

- abstract channel behavior
- email and SMS sending behavior
- push notification output
- notification delivery through all channels
- user order creation and cancellation
- password validation
- sending a message to another user

## Notes

This project uses a lightweight simulation approach rather than real email/SMS delivery. The goal is to model the system design and the communication workflow in an object-oriented way.
