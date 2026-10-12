# Stock Portfolio Tracker 📈

## About the Project

A command-line Stock Portfolio Tracker built with Python as part of my CodeAlpha Python Programming Internship tasks.

The program allows users to select stocks, specify quantities, calculate their total investment, and save a detailed report of their portfolio.

## Features

* **Stock Selection:** Supports AAPL, TSLA, GOOGL, MSFT, and AMZN.
* **Investment Calculation:** Calculates the investment value of each stock based on its predefined price and quantity.
* **Multiple Stock Entries:** Allows users to add multiple stocks to their portfolio.
* **Input Validation:** Handles invalid stock names, non-numeric quantities, and quantities that are zero or negative.
* **Interactive Prompts:** Validates user responses when deciding whether to add another stock or save results.
* **Portfolio Reporting:** Displays the total portfolio investment.
* **File Handling:** Saves a detailed portfolio report to `portfolio_results.txt` when requested.

## Technologies Used

* Python 3
* Dictionaries
* Lists
* Loops and conditional statements
* Exception handling
* File handling

## Stock Prices

The program uses the following predefined stock prices:

| Stock Symbol | Price per Share |
| ------------ | --------------: |
| AAPL         |            $180 |
| TSLA         |            $250 |
| GOOGL        |            $150 |
| MSFT         |            $400 |
| AMZN         |            $200 |

*Note: These are predefined sample prices and are not live market prices.*

## How to Run

1. Ensure Python 3 is installed on your computer.

2. Clone this repository or download the project files.

3. Open a terminal in the project directory.

4. Run the program:

   ```bash
   python stock_tracker.py
   ```

5. Follow the prompts to select stocks, enter quantities, and calculate your portfolio investment.

6. Choose whether to save your results to a text file.

## Example Output

```text
Enter the stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): GOOGL
Enter the quantity: 8
Do you want to add another stock? (yes/no): no
Total portfolio investment: $ 1200
Do you want to save your results? (yes/no): yes
Results saved to portfolio_results.txt
```

## What I Learned

Through this project, I practiced working with Python dictionaries and lists, implementing loops and conditional statements, validating user input, handling exceptions, performing calculations, and writing data to text files.

## Author

Meshack

**Python Programming Intern — CodeAlpha**
