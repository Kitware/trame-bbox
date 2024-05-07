export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame_bbox",
      formats: ["umd"],
      fileName: "trame-bbox",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../trame_bbox/module/serve",
    assetsDir: ".",
  },
};
