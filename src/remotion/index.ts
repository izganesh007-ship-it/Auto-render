import { AbsoluteFill, Audio, Img, useCurrentFrame, registerRoot, Composition, staticFile } from 'remotion';
import React from 'react';

const images = ['image1.jfif', 'image2.jfif', 'image3.jfif', 'image4.jfif', 'image5.jfif'];

const Scene: React.FC = () => {
  const frame = useCurrentFrame();
  const imageIndex = Math.floor(frame / 150) % images.length;
  const currentImage = images[imageIndex];

  return (
    <AbsoluteFill style={{ backgroundColor: '#000080' }}>
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <Img 
          src={staticFile(`assets/${currentImage}`)} 
          style={{ width: '100%', height: '100%', objectFit: 'cover' }} 
        />
      </AbsoluteFill>
      <Audio src={staticFile('voiceover.mp3')} />
    </AbsoluteFill>
  );
};

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="DynamicComp"
      component={Scene}
      durationInFrames={750}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};

registerRoot(RemotionRoot);
