// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package athena

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an Athena Named Query resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/athena"
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/kms"
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/s3"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		hogeBucket, err := s3.NewBucket(ctx, "hogeBucket", nil)
// 		if err != nil {
// 			return err
// 		}
// 		testKey, err := kms.NewKey(ctx, "testKey", &kms.KeyArgs{
// 			DeletionWindowInDays: pulumi.Int(7),
// 			Description:          pulumi.String("Athena KMS Key"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testWorkgroup, err := athena.NewWorkgroup(ctx, "testWorkgroup", &athena.WorkgroupArgs{
// 			Configuration: &athena.WorkgroupConfigurationArgs{
// 				ResultConfiguration: &athena.WorkgroupConfigurationResultConfigurationArgs{
// 					EncryptionConfiguration: &athena.WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs{
// 						EncryptionOption: pulumi.String("SSE_KMS"),
// 						KmsKeyArn:        testKey.Arn,
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		hogeDatabase, err := athena.NewDatabase(ctx, "hogeDatabase", &athena.DatabaseArgs{
// 			Name:   pulumi.String("users"),
// 			Bucket: hogeBucket.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = athena.NewNamedQuery(ctx, "foo", &athena.NamedQueryArgs{
// 			Workgroup: testWorkgroup.ID(),
// 			Database:  hogeDatabase.Name,
// 			Query: hogeDatabase.Name.ApplyT(func(name string) (string, error) {
// 				return fmt.Sprintf("%v%v%v", "SELECT * FROM ", name, " limit 10;"), nil
// 			}).(pulumi.StringOutput),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type NamedQuery struct {
	pulumi.CustomResourceState

	// The database to which the query belongs.
	Database pulumi.StringOutput `pulumi:"database"`
	// A brief explanation of the query. Maximum length of 1024.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The plain language name for the query. Maximum length of 128.
	Name pulumi.StringOutput `pulumi:"name"`
	// The text of the query itself. In other words, all query statements. Maximum length of 262144.
	Query pulumi.StringOutput `pulumi:"query"`
	// The workgroup to which the query belongs. Defaults to `primary`
	Workgroup pulumi.StringPtrOutput `pulumi:"workgroup"`
}

// NewNamedQuery registers a new resource with the given unique name, arguments, and options.
func NewNamedQuery(ctx *pulumi.Context,
	name string, args *NamedQueryArgs, opts ...pulumi.ResourceOption) (*NamedQuery, error) {
	if args == nil || args.Database == nil {
		return nil, errors.New("missing required argument 'Database'")
	}
	if args == nil || args.Query == nil {
		return nil, errors.New("missing required argument 'Query'")
	}
	if args == nil {
		args = &NamedQueryArgs{}
	}
	var resource NamedQuery
	err := ctx.RegisterResource("aws:athena/namedQuery:NamedQuery", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNamedQuery gets an existing NamedQuery resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNamedQuery(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NamedQueryState, opts ...pulumi.ResourceOption) (*NamedQuery, error) {
	var resource NamedQuery
	err := ctx.ReadResource("aws:athena/namedQuery:NamedQuery", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NamedQuery resources.
type namedQueryState struct {
	// The database to which the query belongs.
	Database *string `pulumi:"database"`
	// A brief explanation of the query. Maximum length of 1024.
	Description *string `pulumi:"description"`
	// The plain language name for the query. Maximum length of 128.
	Name *string `pulumi:"name"`
	// The text of the query itself. In other words, all query statements. Maximum length of 262144.
	Query *string `pulumi:"query"`
	// The workgroup to which the query belongs. Defaults to `primary`
	Workgroup *string `pulumi:"workgroup"`
}

type NamedQueryState struct {
	// The database to which the query belongs.
	Database pulumi.StringPtrInput
	// A brief explanation of the query. Maximum length of 1024.
	Description pulumi.StringPtrInput
	// The plain language name for the query. Maximum length of 128.
	Name pulumi.StringPtrInput
	// The text of the query itself. In other words, all query statements. Maximum length of 262144.
	Query pulumi.StringPtrInput
	// The workgroup to which the query belongs. Defaults to `primary`
	Workgroup pulumi.StringPtrInput
}

func (NamedQueryState) ElementType() reflect.Type {
	return reflect.TypeOf((*namedQueryState)(nil)).Elem()
}

type namedQueryArgs struct {
	// The database to which the query belongs.
	Database string `pulumi:"database"`
	// A brief explanation of the query. Maximum length of 1024.
	Description *string `pulumi:"description"`
	// The plain language name for the query. Maximum length of 128.
	Name *string `pulumi:"name"`
	// The text of the query itself. In other words, all query statements. Maximum length of 262144.
	Query string `pulumi:"query"`
	// The workgroup to which the query belongs. Defaults to `primary`
	Workgroup *string `pulumi:"workgroup"`
}

// The set of arguments for constructing a NamedQuery resource.
type NamedQueryArgs struct {
	// The database to which the query belongs.
	Database pulumi.StringInput
	// A brief explanation of the query. Maximum length of 1024.
	Description pulumi.StringPtrInput
	// The plain language name for the query. Maximum length of 128.
	Name pulumi.StringPtrInput
	// The text of the query itself. In other words, all query statements. Maximum length of 262144.
	Query pulumi.StringInput
	// The workgroup to which the query belongs. Defaults to `primary`
	Workgroup pulumi.StringPtrInput
}

func (NamedQueryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*namedQueryArgs)(nil)).Elem()
}
