
class Queue:
    # the constructor initializes the queue with a list of tickets each person needs
    def __init__(self, tickets=[]):
        # self.queue is where we store the people in the queue
        self.queue=[]

        for index, ticket_count in enumerate(tickets):# enumerate(tickets) gives us both the person's index and the number of tickets they need
            pair= (index, ticket_count) # create a tuple of (index, ticket_count) for each person in the queue
            self.queue.append(pair) # append the tuple to the queue

    # this method simulates the process of buying tickets
    def buy_tickets(self, k):
        # initialize a variable to track the number of seconds (turns) it takes
        seconds= 0

        while len(self.queue) > 0: # loop while there are still people in the queue
            person= self.queue.pop(0) # pop the first person from the queue
            index, ticket_count= person # unpack the tuple into index and ticket_count

            ticket_count -=1 # subtract one ticket from the person's remaining tickets
            seconds +=1 # increment the time counter by 1 second

            # check if this person has finished buying all their tickets and if they are the person we're tracking
            if ticket_count==0 and index == k:
                return seconds # If the person at index k has no more tickets, return the calculated time
            
            # if the person still needs tickets, they go back to the end of the queue
            if ticket_count > 0:
                self.queue.append((index, ticket_count))  # append the person back into the queue with the updated ticket count