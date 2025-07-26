import { useState } from "react";

export default function Name({
  HolderContainer = "div",
  className,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer id={_id} className={className} {...props}>
        {children}
      </HolderContainer>
    </>
  );
}
