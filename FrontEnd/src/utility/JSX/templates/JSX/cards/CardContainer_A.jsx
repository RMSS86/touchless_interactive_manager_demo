import { useState } from "react";
import "./CardContainer.scss";
const _cardCLass = "card";
export default function CardContainer({
  HolderContainer = "div",
  className,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer
        id={_id}
        className={`${_cardCLass} ${className}`}
        {...props}
      >
        {children}
      </HolderContainer>
    </>
  );
}
