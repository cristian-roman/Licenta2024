import { keyframes } from "@emotion/react";


const getGrowAnimation = (from, to) => keyframes`
  from {
    font-size: ${from}rem;
  }
  to {
    font-size: ${to}rem;
  }
`;

export function growAnimation(from = 1, to = 3) {
  return { animation: `${getGrowAnimation(from, to)} 1s ease-in-out forwards` };
}


const fadeInFrames = keyframes`
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
`;


export function fadeIn() {
  return `${fadeInFrames} 1s ease-in-out forwards`;
}