const state = {
	list: [],
	type: [],
	id:0
}
 
const mutations = {
	change(state, n) {
		console.log(n)
		state.list = n
	},
	changetype(state,type){
		console.log(type)
		state.type = type
	},
	changeid(state,id){
		console.log(id)
		state.id = id
	}
}
 
 
export default {
	namespaced: true,
	state,
	mutations
}