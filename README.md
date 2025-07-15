# Queue Ticket Buying Simulation

## Description
This Python program simulates the process of people in a queue buying tickets, one per second, until the person at index `k` finishes all their tickets. It tracks how many seconds it takes for the person at index `k` to complete their purchase.

## Class: `Queue`

### `__init__(self, tickets=[])`
- **Purpose**: Initializes the queue with people and their ticket counts.
- **Parameters**: `tickets` — a list where each element represents the number of tickets a person wants.

### `buy_tickets(self, k)`
- **Purpose**: Simulates the ticket-buying process and returns the time it takes for the person at index `k` to finish.
- **Parameters**: `k` — the index of the person being tracked.

