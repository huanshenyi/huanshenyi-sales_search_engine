<template>
    <div class="contactt">
        <Layout>
            <div slot="container">
                <div ref="myChart" :style="{width: '100%', height: '100%'}">
                    kokomap
                </div>
            </div>
        </Layout>
    </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
@Component({
    components:{Layout}
})
export default class Contactt extends Vue{

}
</script>

<style scoped lang="scss">

</style>