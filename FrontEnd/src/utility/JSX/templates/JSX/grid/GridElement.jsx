import { useState } from "react";

export default function GridElement({
  HolderContainer = "div",
  className,
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer className={className} {...props}>
        {children}
      </HolderContainer>
    </>
  );
}
