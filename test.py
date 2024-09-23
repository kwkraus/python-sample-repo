# %%
message = "hello kevin, this is my first message through python, not really but it's a start"

print(message)

# %%
nextmsg = "this is the second message, I'm getting the hang of this"

print(nextmsg)

# %%
x = 22

y = 7

print(x + y)

# %%
#create a function that does the calculation of mortgage rate ammortization
def mortgage_rate(principal, rate, time):
    #formula for calculating mortgage rate
    return principal * rate * time

print(mortgage_rate(100000, 0.05, 30))

# %%
