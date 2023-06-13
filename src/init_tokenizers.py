import argparse
from args import add_args
import enums
from data.dataset import init_dataset
from data.vocab import init_vocab, load_vocab
from data.data_collator import collate_fn


def init_all(args):

	dataset_code2code_train =  init_dataset(args=args, mode=enums.TRAINING_MODE_FINE_TUNE, task=enums.TASK_CODE2CODE, split='train',load_if_saved=False)
	dataset_code2code_valid =  init_dataset(args=args, mode=enums.TRAINING_MODE_FINE_TUNE, task=enums.TASK_CODE2CODE, split='valid',load_if_saved=False)
	dataset_code2code_test =  init_dataset(args=args, mode=enums.TRAINING_MODE_FINE_TUNE, task=enums.TASK_CODE2CODE, split='test',load_if_saved=False)

	# code vocab
	code_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
	                        name=args.code_vocab_name,
	                        method=args.code_tokenize_method,
	                        vocab_size=args.code_vocab_size,
	                        datasets=[
								dataset_code2code_train.codes, dataset_code2code_train.targets, \
								dataset_code2code_valid.codes, dataset_code2code_valid.targets, \
								dataset_code2code_test.codes, dataset_code2code_test.targets
	                        ],
	                        ignore_case=True,
	                        save_root=args.vocab_root,
	                        load_if_saved=False)

def load_and_test(args):
	code_vocab = load_vocab(vocab_root=args.vocab_root, name=args.code_vocab_name)

	# print(code_vocab.encode_sequence('public double METHOD_1 ( TYPE_1 VAR_1 ) { if ( ( this ) == VAR_1 ) return VAR_2 ; if ( ( this . y ) == ( VAR_1 . y ) ) return VAR_3 ; return ( ( VAR_1 . y ) - ( this . y ) ) / ( ( VAR_1 . x ) - ( this . x ) ) ; }'))
	# print(code_vocab.decode(code_vocab.encode_sequence('METHOD_1')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('METHOD_2')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('METHOD_3')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('METHOD_4')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('METHOD_5')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('INT_1')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('VAR_1')[0]))
	# print(code_vocab.decode(code_vocab.encode_sequence('TYPE_1')[0]))

	batches = {
		enums.TASK_METHOD_NAME_PREDICTION: [
			[
				'TASK_METHOD_NAME_PREDICTION: public ImageSource apply ( ImageSource input ) {return source ; }',
				'apply'
			],
			[
				'TASK_METHOD_NAME_PREDICTION: static void myMethod() { System.out.println("I just got executed!");}',
				'myMethod'
			],
			[
				'TASK_METHOD_NAME_PREDICTION: public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'main'
			]
		],
		enums.TASK_RTD: [
			[
				'TASK_RTD: public ImageSource apply ( ImageSource input ) {return source ; }',
				'1 0 0 0 1 1 0 1 1 1 0'
			],
			[
				'TASK_RTD: static void myMethod() { System.out.println("I just got executed!");}',
				'1 1 1 0 0 0'
			],
			[
				'TASK_RTD: public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'0 1 1 1 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1'
			]
		],
		enums.TASK_AUTOCOMPLETION: [
			[
				'TASK_AUTOCOMPLETION: public ImageSource apply ( ImageSource input )',
				'{return source ; }'
			],
			[
				'TASK_AUTOCOMPLETION: static void myMethod(',
				') { System.out.println("I just got executed!");}'
			],
			[
				'TASK_AUTOCOMPLETION: public static void main(String[] args) { myMethod("Liam")',
				'; myMethod("Jenny"); myMethod("Anja");}'
			]
		],
		enums.TASK_CODE_AST_PREDICTION: [
			[
				'TASK_CODE_AST_PREDICTION: public ImageSource apply ( ImageSource input ) {return source ; }[SEP]local_variable_declaration return_statement__ object_creation_expression __return_statement',
				'1'
			],
			[
				'TASK_CODE_AST_PREDICTION: static void myMethod() { System.out.println("I just got executed!");}[SEP]if_statement__ parenthesized_expression__ binary_expression __parenthesized_expression return_statement __if_statement local_variable_declaration return_statement__ ternary_expression__ binary_expression __ternary_expression __return_statement',
				'0'
			],
			[
				'TASK_CODE_AST_PREDICTION: public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}[SEP]try_statement__ expression_statement expression_statement expression_statement __try_statement',
				'1'
			]
		],
		enums.TASK_MASS: [
			[
				'TASK_MASS: public ImageSource apply ( [MASK] ) {return source ; }',
				'ImageSource input'
			],
			[
				'TASK_MASS: [MASK] { System.out.println("I just got executed!");}',
				'static void myMethod()'
			],
			[
				'TASK_MASS: public static void main(String[] args) { myMethod("Liam"); [MASK]}',
				'myMethod("Jenny"); myMethod("Anja");'
			]
		],
		enums.TASK_MLM: [
			[
				'TASK_MASS: public ImageSource apply ( [MASK] ) {return [MASK] ; }',
				'public ImageSource apply ( ImageSource input ) {return source ; }'
			],
			[
				'TASK_MASS: static [MASK] myMethod() { System.out.println("I just [MASK] executed!");}',
				'static void myMethod() { System.out.println("I just got executed!");}'
			],
			[
				'TASK_MASS: public [MASK] void main(String[] [MASK]) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}'
			]
		],
		enums.TASK_MIP: [
			[
				'TASK_MASS: public ImageSource apply ( [MASK] ) {return [MASK] ; }',
				'public ImageSource apply ( ImageSource input ) {return source ; }'
			],
			[
				'TASK_MASS: static [MASK] myMethod() { System.out.println("I just [MASK] executed!");}',
				'static void myMethod() { System.out.println("I just got executed!");}'
			],
			[
				'TASK_MASS: public [MASK] void main(String[] [MASK]) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}'
			]
		],
		enums.TASK_IDENTIFIER_TAGGING: [
			[
				'TASK_IDENTIFIER_TAGGING: public ImageSource apply ( ImageSource input ) {return source ; }',
				'1 0 0 0 1 1 0 1 1 1 0'
			],
			[
				'TASK_IDENTIFIER_TAGGING: static void myMethod() { System.out.println("I just got executed!");}',
				'1 1 1 0 0 0'
			],
			[
				'TASK_IDENTIFIER_TAGGING: public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'0 1 1 1 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1'
			]
		],
		enums.TASK_METHOD_DOCS_PREDICTION: [
			[
				'TASK_METHOD_DOCS_PREDICTION: public ImageSource apply ( ImageSource input ) {return source ; }',
				'Expects a height mat as input param input A grayscale height map return edges'
			],
			[
				'TASK_METHOD_DOCS_PREDICTION: static void myMethod() { System.out.println("I just got executed!");}',
				'Pops the top event off the current event stack This action has to be performed immediately after the event has been dispatched to all listeners param Type of the listener param expected The Event which is expected at the top of the stack pushEvent'
			],
			[
				'TASK_METHOD_DOCS_PREDICTION: public static void main(String[] args) { myMethod("Liam"); myMethod("Jenny"); myMethod("Anja");}',
				'Executes the given transaction within the context of a write lock param t The transaction to execute'
			]
		]
	}

	dataset_pre_trained = init_dataset(args=args, mode=enums.TRAINING_MODE_PRE_TRAIN)
	for task, batch in batches.items():
		print('######################################################')
		dataset_pre_trained.set_task(task)
		print(task)
		print(collate_fn(batch, args, dataset_pre_trained, code_vocab, nl_vocab, ast_vocab)	)

	# dataset_bug_fix_small_train =  init_dataset(args=args, mode=enums.TRAINING_MODE_FINE_TUNE, task=enums.TASK_BUG_FIX, language='small', split='train')

	# batches = {
	# 	enums.TASK_BUG_FIX: [
	# 		[
	# 			"TASK_BUG_FIX: public VmBase() { <START> mOs = VmOsType.Unassigned; <END> }[SEP]remove initializing c'tor is done declaration statement: private VmOsType mOs = VmOsType.Unassigned;",
	# 			"public VmBase() { }"
	# 		]
	# 	]
	# }
	# for task, batch in batches.items():
	# 	print('######################################################')
	# 	# dataset_pre_trained.set_task(task)
	# 	print(task)
	# 	print(collate_fn(batch, args, dataset_bug_fix_small_train, code_vocab, nl_vocab, ast_vocab))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.register('type', 'bool', lambda v: v.lower() in ['yes', 'true', 't', '1', 'y'])

	add_args(parser)

	main_args = parser.parse_args()
	main_args.vocab_root = main_args.vocab_save_dir
	print(main_args.vocab_save_dir)

	# initialize tokenizers for a new dataset.
	# In the first iteration, one needs to initialize the tokenizers, then in the following iterations one can ensure with load_and_test() if it is tokenized properly
	init_all(main_args)
	#load_and_test(main_args)
