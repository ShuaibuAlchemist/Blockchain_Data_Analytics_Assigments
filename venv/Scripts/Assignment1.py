# %% [markdown]
# Python problems on Datastructure
# 
#  Problem 1: Cryptocurrency Token Data
# This data structure represents information about different cryptocurrency tokens listed on a decentralized exchange (DEX).
# 

# %%
crypto_tokens = [
    {
        "name": "Token A",
        "symbol": "TKA",
        "blockchain": "Ethereum",
        "current_price_usd": 100.0,
        "transaction_history": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 98.0,
                    "close": 100.0,
                    "high": 101.0,
                    "low": 97.0
                },
                "volume": 12000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 97.0,
                    "close": 98.0,
                    "high": 99.0,
                    "low": 96.0
                },
                "volume": 15000
            }
        ],
        "supported_chains": ["Ethereum", "Polygon"]
    },
    {
        "name": "Token B",
        "symbol": "TKB",
        "blockchain": "Binance Smart Chain",
        "current_price_usd": 200.0,
        "transaction_history": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 198.0,
                    "close": 200.0,
                    "high": 202.0,
                    "low": 196.0
                },
                "volume": 18000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 196.0,
                    "close": 198.0,
                    "high": 199.0,
                    "low": 195.0
                },
                "volume": 17000
            }
        ],
        "supported_chains": ["Binance Smart Chain", "Avalanche"]
    },
    {
        "name": "Token C",
        "symbol": "TKC",
        "blockchain": "Solana",
        "current_price_usd": 300.0,
        "transaction_history": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 295.0,
                    "close": 300.0,
                    "high": 302.0,
                    "low": 294.0
                },
                "volume": 22000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 294.0,
                    "close": 295.0,
                    "high": 296.0,
                    "low": 293.0
                },
                "volume": 21000
            }
        ],
        "supported_chains": ["Solana", "Fantom"]
    }
]


# %% [markdown]
# Q1: Read Data  
# Task: Display the current price of "Token B".
# 

# %%
crypto_tokens[1]["current_price_usd"]

# %% [markdown]
# Q2: Write Data  
# Task: Add a new token "Token D" with some initial data to the `crypto_tokens` list

# %%
crypto_tokens.append(    {
        "name": "Token D",
        "symbol": "BTC",
        "blockchain": "Bitcoin",
        "current_price_usd": 1300.0,
        "transaction_history": [
            {
                "date": "2024-07-11",
                "prices": {
                    "open": 118.0,
                    "close": 900.0,
                    "high": 131.0,
                    "low": 77.0
                },
                "volume": 12000
            },
            {
                "date": "2024-07-11",
                "prices": {
                    "open": 107.0,
                    "close": 98.0,
                    "high": 109.0,
                    "low": 96.0
                },
                "volume": 15000
            }
        ],
        "supported_chains": ["Ethereum", "Polygon"]
    })

crypto_tokens

# %% [markdown]
# Q3: Update Data  
# Task: Update the current price of "Token C" to 310.0.

# %%
crypto_tokens[2]["current_price_usd"] = 310.0

# %% [markdown]
# Q4: Delete Data  
# Task: Remove the transaction history for "Token A" on "2024-01-09".
# 

# %%
crypto_tokens[0]['transaction_history'].remove({
                "date": "2024-01-09",
                "prices": {
                    "open": 97.0,
                    "close": 98.0,
                    "high": 99.0,
                    "low": 96.0
                },
                "volume": 15000
            })

crypto_tokens

# %% [markdown]
# Q5: Read Nested Data  
# Task: Display the closing price of "Token B" on "2024-01-10".

# %%
crypto_tokens[1]['transaction_history'][0]['prices']['close']

# %% [markdown]
# Q7: Add Nested Data  
# Task: Add a new transaction history entry for "Token C" on "2024-01-11

# %%
crypto_tokens[2]['transaction_history'].append({"date":"2024-01-10","prices": {"open": 295.0,"close": 300.0,"high": 302.0,"low": 294.0}, "volume": 22000})

crypto_tokens

# %% [markdown]
# Q8: Delete an Item from a List Inside a Dictionary  
# Task: Remove "Avalanche" from the supported chains of "Token B

# %%
crypto_tokens[1]['supported_chains'].remove('Avalanche')
crypto_tokens


