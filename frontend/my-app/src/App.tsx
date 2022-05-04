import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "./routes/Home";
import { LoginSuccess } from "./routes/LoginSuccess";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route index element={<Home />} />
        </Route>
        <Route path="/success">
          <Route index element={<LoginSuccess />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
