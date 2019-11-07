<template>
  <div class="py-8 bg-gray-100">
    <div class="container">
      <h1 class="font-semibold text-gray-700">
        Styleguide
      </h1>

      <styleguide-section title="Typography">
        <styleguide-typography />
      </styleguide-section>

      <styleguide-section title="Icons">
        <styleguide-icons />
      </styleguide-section>

      <styleguide-section title="Form elements">
        <styleguide-form-elements />
      </styleguide-section>

      <styleguide-section title="Button">
        <button class="btn">A button</button>
        <!-- <input class="btn" type="submit" value="A button" /> -->
      </styleguide-section>

      <styleguide-section title="Tooltip and Popover">
        <section-tooltip />
      </styleguide-section>

      <styleguide-section title="Forge Toggle">
        <forge-toggle>
          Inline Toggle
          <p slot="body">Lorem ipsum dolor sit amet.</p>
        </forge-toggle>

        <section-sub title="Block">
          <forge-toggle
            class="mt-4"
            class-button="block w-full"
            class-body="mt-4 border rounded"
          >
            Im block toggle, rounded and with a border
            <p slot="body">Lorem ipsum dolor sit amet.</p>
          </forge-toggle>
        </section-sub>
      </styleguide-section>
    </div>
  </div>
</template>

<script>
import StyleguideSection from '@/styleguide/Section';
import SectionSub from '@/styleguide/SectionSub';
import StyleguideTypography from '@/styleguide/Typography';
import StyleguideFormElements from '@/styleguide/FormElements';
import StyleguideIcons from '@/styleguide/Icons';
import SectionTooltip from '@/styleguide/SectionTooltip';
import ForgeToggle from '@/components/Toggle';

export default {
  components: {
    StyleguideSection,
    SectionSub,
    StyleguideTypography,
    StyleguideIcons,
    StyleguideFormElements,
    SectionTooltip,
    ForgeToggle,
  },
};
</script>
