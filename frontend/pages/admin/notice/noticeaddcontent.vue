<template>
	<u-form style="margin-left: 30rpx;margin-right: 30rpx; margin-top: 20rpx;">
		<u-form-item label="标题" ><u-input v-model="title"/></u-form-item>
		<u-form-item label="紧急程度">
			<u-radio-group>
				<u-radio v-for="(item, index) in priority" :disabled="item.disabled" :name="item.name" @change="change(item.name)">
					{{item.name}}
				</u-radio>
			</u-radio-group>
		</u-form-item>
		<u-form-item label="内容"><u-input v-model="content"/></u-form-item>
		<u-form-item>
			<button @click="click()">提交</button>
			<u-toast ref="uToast" />
			<u-modal v-model="show" :content="confirm" :show-cancel-button=true @confirm="confirm_()"></u-modal>
		</u-form-item>
	</u-form>
</template>

<script>
	export default {
		data() {
			return {
				show:false,
				confirm:"确认提交？",
				title:'',
				content:'',
				priority:[
					{
						name:"普通",
						disabled:false,
						check:false,
					},
					{
						name:"重要",
						disabled:false,
						check:false,
					},
					{
						name:"紧急",
						disabled:false,
						check:false,
					}
				],
				pri:'',
			}
		},
		methods: {
			change(priority){
				this.pri=priority;
				// console.log(this.pri);
			},
			click(){
				if(this.pri=='' || this.content=='' || this.title==''){
					this.$refs.uToast.show({
						title: '请完善内容',
						type: 'error',
					})
				}
				else{
					this.show=true;
				}
			},
			confirm_(){
				console.log("提交成功");
				this.$refs.uToast.show({
					title: '提交成功',
					type: 'success',
				});
				uni.navigateTo({
					url: '../noticeadd',
				});
				
			},
		}
	}
</script>

<style>

</style>
