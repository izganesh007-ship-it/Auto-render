import {AbsoluteFill, Audio, Img, interpolate, spring, useCurrentFrame, useVideoConfig, registerRoot, Composition} from 'remotion';
import {staticFile} from 'remotion';
import React from 'react';

const MainScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();

  const images = [
    staticFile('assets/image1.jpg'),
    staticFile('assets/image2.jpg'),
    staticFile('assets/image3.jpg'),
    staticFile('assets/image4.jpg'),
  ];

  const imageIndex = Math.floor(frame / 150) % images.length;
  const image = images[imageIndex];

  const scale = spring({
    frame,
    fps,
    from: 1,
    to: 1.1,
    config: {
      damping: 100,
    },
  });

  return (
    <AbsoluteFill style={{backgroundColor: 'white'}}>
      <Img
        src={image}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${scale})`,
        }}
      />
      <Audio src={staticFile('voiceover.mp3')} />
    </AbsoluteFill>
  );
};

const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="DynamicComp"
        component={MainScene}
        durationInFrames={750}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};

registerRoot(RemotionRoot);