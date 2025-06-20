import React from "react";
import { render, screen } from "@testing-library/react";
import App from "../src/App";

test("renders dashboard title", () => {
  render(<App />);
  expect(screen.getByText(/Hybrid Cloud Manager/i)).toBeInTheDocument();
});