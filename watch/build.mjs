import { mkdirSync, copyFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve, join } from 'node:path';
import { spawnSync } from 'node:child_process';

const source = dirname(fileURLToPath(import.meta.url));
const project = resolve(source, '..');
const output = resolve(process.argv[2] ?? join(source, 'dist'));
mkdirSync(output, { recursive: true });
copyFileSync(join(source, 'index.html'), join(output, 'index.html'));
const video = join(project, 'renders', 'ChatGPT-四周年致敬-1080p.mp4');
const run = args => {
  const result = spawnSync('ffmpeg', ['-y', '-hide_banner', '-loglevel', 'error', ...args], { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
};
run(['-i', video, '-c', 'copy', '-movflags', '+faststart', join(output, 'film.mp4')]);
run(['-ss', '2.5', '-i', video, '-frames:v', '1', '-q:v', '3', join(output, 'poster.jpg')]);
console.log('Built static video player:', output);
