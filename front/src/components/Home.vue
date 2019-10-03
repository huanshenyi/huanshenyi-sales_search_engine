<template>
    <div class="home">
        <Layout>
            <div slot="container">
                <h1>home</h1>
            </div>
        </Layout>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
@Component({
    components:{Layout}
})
export default class Contactt extends Vue{

}
</script>

<style scoped lang="scss">

</style>