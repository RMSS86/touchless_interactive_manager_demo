import { useState } from "react";

export default function NavElement({
  HolderContainer = "li",
  _className,
  _aClass,
  _navIndex,
  _navTitle,
  _href,
  _key,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer id={_id} className={_className} {...props}>
        <a href={_href} className={_aClass}>
          <span>{_navIndex}</span>
          {_navTitle}
        </a>
      </HolderContainer>
    </>
  );
}
