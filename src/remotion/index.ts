import {AbsoluteFill, Audio, Img, interpolate, spring, useCurrentFrame, useVideoConfig, registerRoot, Composition, staticFile} from 'remotion';

const MainScene = () => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();

  const images = [
    staticFile('assets/image1.png'),
    staticFile('assets/image2.png'),
    staticFile('assets/image3.png'),
  ];

  const imageIndex = Math.min(Math.floor(frame / 30), images.length - 1);
  const image = images[imageIndex];

  return (
    <AbsoluteFill style={{backgroundColor: '#000080', justifyContent: 'center', alignItems: 'center'}}>
      <Img src={image} style={{width: width * 0.8, height: height * 0.8, objectFit: 'contain'}} />
      <Audio src={staticFile('voiceover.mp3')} />
    </AbsoluteFill>
  );
};

const RemotionRoot = () => {
  return (
    <Composition
      id="DynamicComp"
      component={MainScene}
      durationInFrames={750}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};

registerRoot(RemotionRoot);