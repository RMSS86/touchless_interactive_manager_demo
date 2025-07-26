import "../../../sass/components/templates/bottons/AnimatedBotton_A.scss";

export default function AnimatedBotton_A({
  ButtonContainer = "a",
  children,
  isSelected = false,
  buttonText,
  btnClasses,
  _href = "#",
  ...props
}) {
  return (
    <>
      <ButtonContainer href={_href} {...props} className={btnClasses}>
        {buttonText}
      </ButtonContainer>
    </>
  );
}
