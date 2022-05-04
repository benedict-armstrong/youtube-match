import * as React from "react";
import GoogleButton from "react-google-button";

export interface IGoogleButtonProps {
  onClick: (uuid: string | null) => void;
  uuid: string | null;
}

export function GoogleButtonComponent(props: IGoogleButtonProps) {
  const handleClick = () => {
    props.onClick(props.uuid);
  };

  return <GoogleButton onClick={handleClick} />;
}
