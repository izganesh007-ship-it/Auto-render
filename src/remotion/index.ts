import {AbsoluteFill, Audio, Img, useCurrentFrame, registerRoot, Composition, staticFile} from 'remotion';
import React from 'react';

const images = ['image1.jfif', 'image2.jfif', 'image3.jfif', 'image4.jfif', 'image5.jfif'];

const Scene: React.FC = () => {
  const frame = useCurrentFrame();
  const imageIndex = Math.floor(frame / 150) % images.length;
  const image = images[imageIndex];

  return (
    <AbsoluteFill style={{backgroundColor: '#000080'}}>
      <Img src={staticFile('assets/' + image)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      <Audio src={staticFile('voiceover.mp3')} />
    </AbsoluteFill>
  );
};

registerRoot(() => (
  <Composition
    id="DynamicComp"
    component={Scene}
    durationInFrames={750}
    fps={30}
    width={1920}
    height={1080}
  />
));
