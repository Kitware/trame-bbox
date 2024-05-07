import { toRefs } from "vue";

export default {
  emits: ["update:modelValue"],
  props: {
    width: {
      type: Number,
      default: 300,
    },
    height: {
      type: Number,
      default: 300,
    },
    modelValue: {
      type: Object,
    },
    readOnly: {
      type: Boolean,
      default: false,
    },
    defaultRectStyle: {
      type: Object,
      default: () => ({
        stroke: "red",
        fill: "white",
        fillOpacity: 0.1,
        strokeWidth: 2,
      }),
    },
  },
  setup(props) {
    const { width, height, readOnly, modelValue, defaultRectStyle } =
      toRefs(props);
    return { width, height, readOnly, modelValue, defaultRectStyle };
  },
  template: `
    <svg version="1.1" :width="width" :height="height" xmlns="http://www.w3.org/2000/svg">
      <rect 
        v-for="item, name in  modelValue"
        :key="name"
        :x="item.x"
        :y="item.y"
        :width="item.width"
        :height="item.height"
        v-bind="{ ...defaultRectStyle, ...item.style}"
      />
    </svg>
  `,
};
