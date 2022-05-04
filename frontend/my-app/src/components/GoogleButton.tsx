import * as React from "react";
import GoogleButton from "react-google-button";

export interface IGoogleButtonProps {
  onClick: () => void;
}

export function GoogleButtonComponent(props: IGoogleButtonProps) {
  return <GoogleButton onClick={props.onClick} />;
}
