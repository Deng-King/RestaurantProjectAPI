const waiter= [
	// 首页
	{
		// 未点击图标
		// iconPath: "/static/tabbar/box.png",
		// 点击后图标
		// selectedIconPath: "/static/tabbar/box_normal.png",
		// 显示文字
		
		// 是否显示红点
		// isDot: true,
		// 是否使用自定义图标
		// customIcon: true,
		// 页面路径
		text: '公告',
		pagePath: "/pages/public/notice/notice"
	},
	{
		text: '点餐',
		pagePath: "/pages/waiter/order/table"
	},
	{
		text: '订单',
		pagePath: "/pages/waiter/orderlist/orderlist"
	},
	{
		text: '我的',
		pagePath: "/pages/public/information/selfinformation"
	}
]
 
const cook= [
	{
		text: '公告',
		pagePath: "/pages/public/notice/notice"
	},
	{
		text: '上菜',
		pagePath: "/pages/cook/cookinglist"
	},
	{
		text: '我的',
		pagePath: "/pages/public/information/selfinformation"
	}
]
 
const admin= [
	{
		text: '公告',
		pagePath: "/pages/admin/notice/noticeadd"
	},
	{
		text: '菜品管理',
		pagePath: "/pages/admin/food/foodlist"
	},
	{
		text: '人员管理',
		pagePath: "/pages/admin/staff/stafflist"
	},
	{
		text: '我的',
		pagePath: "/pages/public/information/selfinformation"
	}
]
export default {
	cook,
	admin,
	waiter
}
