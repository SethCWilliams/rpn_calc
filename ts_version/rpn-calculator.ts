import * as readline from "readline";

const OPERATORS: { [key: string]: (a: number, b: number) => number } = {
  "+": (a, b) => a + b,
  "-": (a, b) => a - b,
  "*": (a, b) => a * b,
  "/": (a, b) => a / b,
};
function roundToReadable(value: number): number {
  // Round the value to two decimal places before pushing it onto the stack for readability
  return Math.round(value * 100) / 100;
}

function isValidToken(token: string): boolean {
  return !isNaN(parseFloat(token)) || token in OPERATORS;
}

function handleOperator(
  token: string,
  stack: number[],
  validInput: boolean
): void {
  if (stack.length < 2) {
    console.log(`Error: Not enough operands for operator '${token}'`);
    validInput = false;
    return;
  }
  // can assert that stack.length >= 2 thanks to if statement above
  const operand2 = stack.pop()!;
  const operand1 = stack.pop()!;
  const result = OPERATORS[token](operand1, operand2);
  stack.push(roundToReadable(result));
}

function handleOperand(
  token: string,
  stack: number[],
  validInput: boolean
): void {
  const value = parseFloat(token);
  if (!isNaN(value)) {
    stack.push(roundToReadable(value));
  } else {
    console.log(`Error: Invalid input '${token}'`);
    validInput = false;
  }
}

function rpnCalculator(): void {
  const stack: number[] = [];
  const cliCalculatorInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  cliCalculatorInterface.setPrompt(
    "Enter operand(s) and/or operator(s) (q to quit and c to clear): "
  );

  cliCalculatorInterface.prompt();

  cliCalculatorInterface.on("line", (line: string) => {
    const formattedLine = line.trim().toLowerCase();
    if (formattedLine === "q") {
      cliCalculatorInterface.close();
      return; // Exit the event handler
    } else if (formattedLine === "c") {
      stack.length = 0; // Clear the stack
    } else {
      const tokens = line.trim().split(/\s+/); // Trims whitespace and splits on whitespace
      let validInput = true; // Flag to track input validity
      const prevStack = [...stack]; // Create a copy of the stack

      for (const token of tokens) {
        if (isValidToken(token)) {
          if (token in OPERATORS) {
            handleOperator(token, stack, validInput);
          } else {
            handleOperand(token, stack, validInput);
          }
        } else {
          console.log(`Error: Invalid input '${token}'`);
          validInput = false;
          stack.length = 0; // Reset the stack to its previous state
          stack.push(...prevStack); // Restore the previous stack
        }
      }

      if (validInput && stack.length > 0) {
        console.log("Current Operand Stack:", stack);
      } else if (!validInput) {
        console.log(
          "Invalid input. Please format it correctly with valid inputs."
        );
      }
    }
    cliCalculatorInterface.prompt();
  });

  cliCalculatorInterface.on("close", () => {
    if (stack.length > 0) {
      console.log("Final Operand Stack:", stack);
    }
    console.log("Calculator has been terminated.");
  });
}

if (require.main === module) {
  rpnCalculator();
}
