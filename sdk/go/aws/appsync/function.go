// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AppSync Function.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/appsync"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		testGraphQLApi, err := appsync.NewGraphQLApi(ctx, "testGraphQLApi", &appsync.GraphQLApiArgs{
// 			AuthenticationType: pulumi.String("API_KEY"),
// 			Schema:             pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v", "type Mutation {\n", "  putPost(id: ID!, title: String!): Post\n", "}\n", "\n", "type Post {\n", "  id: ID!\n", "  title: String!\n", "}\n", "\n", "type Query {\n", "  singlePost(id: ID!): Post\n", "}\n", "\n", "schema {\n", "  query: Query\n", "  mutation: Mutation\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testDataSource, err := appsync.NewDataSource(ctx, "testDataSource", &appsync.DataSourceArgs{
// 			ApiId: testGraphQLApi.ID(),
// 			Type:  pulumi.String("HTTP"),
// 			HttpConfig: &appsync.DataSourceHttpConfigArgs{
// 				Endpoint: pulumi.String("http://example.com"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = appsync.NewFunction(ctx, "testFunction", &appsync.FunctionArgs{
// 			ApiId:                   testGraphQLApi.ID(),
// 			DataSource:              testDataSource.Name,
// 			Name:                    pulumi.String("tf_example"),
// 			RequestMappingTemplate:  pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "    \"version\": \"2018-05-29\",\n", "    \"method\": \"GET\",\n", "    \"resourcePath\": \"/\",\n", "    \"params\":{\n", "        \"headers\": ", "$", "utils.http.copyheaders(", "$", "ctx.request.headers)\n", "    }\n", "}\n")),
// 			ResponseMappingTemplate: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v", "#if(", "$", "ctx.result.statusCode == 200)\n", "    ", "$", "ctx.result.body\n", "#else\n", "    ", "$", "utils.appendError(", "$", "ctx.result.body, ", "$", "ctx.result.statusCode)\n", "#end\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Function struct {
	pulumi.CustomResourceState

	// The ID of the associated AppSync API.
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// The ARN of the Function object.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The Function DataSource name.
	DataSource pulumi.StringOutput `pulumi:"dataSource"`
	// The Function description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A unique ID representing the Function object.
	FunctionId pulumi.StringOutput `pulumi:"functionId"`
	// The version of the request mapping template. Currently the supported value is `2018-05-29`.
	FunctionVersion pulumi.StringPtrOutput `pulumi:"functionVersion"`
	// The Function name. The function name does not have to be unique.
	Name pulumi.StringOutput `pulumi:"name"`
	// The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
	RequestMappingTemplate pulumi.StringOutput `pulumi:"requestMappingTemplate"`
	// The Function response mapping template.
	ResponseMappingTemplate pulumi.StringOutput `pulumi:"responseMappingTemplate"`
}

// NewFunction registers a new resource with the given unique name, arguments, and options.
func NewFunction(ctx *pulumi.Context,
	name string, args *FunctionArgs, opts ...pulumi.ResourceOption) (*Function, error) {
	if args == nil || args.ApiId == nil {
		return nil, errors.New("missing required argument 'ApiId'")
	}
	if args == nil || args.DataSource == nil {
		return nil, errors.New("missing required argument 'DataSource'")
	}
	if args == nil || args.RequestMappingTemplate == nil {
		return nil, errors.New("missing required argument 'RequestMappingTemplate'")
	}
	if args == nil || args.ResponseMappingTemplate == nil {
		return nil, errors.New("missing required argument 'ResponseMappingTemplate'")
	}
	if args == nil {
		args = &FunctionArgs{}
	}
	var resource Function
	err := ctx.RegisterResource("aws:appsync/function:Function", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFunction gets an existing Function resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFunction(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FunctionState, opts ...pulumi.ResourceOption) (*Function, error) {
	var resource Function
	err := ctx.ReadResource("aws:appsync/function:Function", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Function resources.
type functionState struct {
	// The ID of the associated AppSync API.
	ApiId *string `pulumi:"apiId"`
	// The ARN of the Function object.
	Arn *string `pulumi:"arn"`
	// The Function DataSource name.
	DataSource *string `pulumi:"dataSource"`
	// The Function description.
	Description *string `pulumi:"description"`
	// A unique ID representing the Function object.
	FunctionId *string `pulumi:"functionId"`
	// The version of the request mapping template. Currently the supported value is `2018-05-29`.
	FunctionVersion *string `pulumi:"functionVersion"`
	// The Function name. The function name does not have to be unique.
	Name *string `pulumi:"name"`
	// The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
	RequestMappingTemplate *string `pulumi:"requestMappingTemplate"`
	// The Function response mapping template.
	ResponseMappingTemplate *string `pulumi:"responseMappingTemplate"`
}

type FunctionState struct {
	// The ID of the associated AppSync API.
	ApiId pulumi.StringPtrInput
	// The ARN of the Function object.
	Arn pulumi.StringPtrInput
	// The Function DataSource name.
	DataSource pulumi.StringPtrInput
	// The Function description.
	Description pulumi.StringPtrInput
	// A unique ID representing the Function object.
	FunctionId pulumi.StringPtrInput
	// The version of the request mapping template. Currently the supported value is `2018-05-29`.
	FunctionVersion pulumi.StringPtrInput
	// The Function name. The function name does not have to be unique.
	Name pulumi.StringPtrInput
	// The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
	RequestMappingTemplate pulumi.StringPtrInput
	// The Function response mapping template.
	ResponseMappingTemplate pulumi.StringPtrInput
}

func (FunctionState) ElementType() reflect.Type {
	return reflect.TypeOf((*functionState)(nil)).Elem()
}

type functionArgs struct {
	// The ID of the associated AppSync API.
	ApiId string `pulumi:"apiId"`
	// The Function DataSource name.
	DataSource string `pulumi:"dataSource"`
	// The Function description.
	Description *string `pulumi:"description"`
	// The version of the request mapping template. Currently the supported value is `2018-05-29`.
	FunctionVersion *string `pulumi:"functionVersion"`
	// The Function name. The function name does not have to be unique.
	Name *string `pulumi:"name"`
	// The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
	RequestMappingTemplate string `pulumi:"requestMappingTemplate"`
	// The Function response mapping template.
	ResponseMappingTemplate string `pulumi:"responseMappingTemplate"`
}

// The set of arguments for constructing a Function resource.
type FunctionArgs struct {
	// The ID of the associated AppSync API.
	ApiId pulumi.StringInput
	// The Function DataSource name.
	DataSource pulumi.StringInput
	// The Function description.
	Description pulumi.StringPtrInput
	// The version of the request mapping template. Currently the supported value is `2018-05-29`.
	FunctionVersion pulumi.StringPtrInput
	// The Function name. The function name does not have to be unique.
	Name pulumi.StringPtrInput
	// The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
	RequestMappingTemplate pulumi.StringInput
	// The Function response mapping template.
	ResponseMappingTemplate pulumi.StringInput
}

func (FunctionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*functionArgs)(nil)).Elem()
}
