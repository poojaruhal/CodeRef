from data.asts.ast_parser import generate_single_ast_nl

ast, nl, nl_wo_name = generate_single_ast_nl(
	source="""
	public static void main() {
    	if (true) {
  			assert true;
		}
  	}
	""",
	lang="java",
	name="some name",
	replace_method_name=True
)
print(ast)
