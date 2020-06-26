// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ebs

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates a Snapshot of an EBS Volume.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ebs"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := ebs.NewVolume(ctx, "example", &ebs.VolumeArgs{
// 			AvailabilityZone: pulumi.String("us-west-2a"),
// 			Size:             pulumi.Int(40),
// 			Tags: pulumi.Map{
// 				"Name": pulumi.String("HelloWorld"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ebs.NewSnapshot(ctx, "exampleSnapshot", &ebs.SnapshotArgs{
// 			Tags: pulumi.Map{
// 				"Name": pulumi.String("HelloWorld_snap"),
// 			},
// 			VolumeId: example.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Snapshot struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The data encryption key identifier for the snapshot.
	DataEncryptionKeyId pulumi.StringOutput `pulumi:"dataEncryptionKeyId"`
	// A description of what the snapshot is.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Whether the snapshot is encrypted.
	Encrypted pulumi.BoolOutput `pulumi:"encrypted"`
	// The ARN for the KMS encryption key.
	KmsKeyId pulumi.StringOutput `pulumi:"kmsKeyId"`
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias pulumi.StringOutput `pulumi:"ownerAlias"`
	// The AWS account ID of the EBS snapshot owner.
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// A map of tags to assign to the snapshot
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The Volume ID of which to make a snapshot.
	VolumeId pulumi.StringOutput `pulumi:"volumeId"`
	// The size of the drive in GiBs.
	VolumeSize pulumi.IntOutput `pulumi:"volumeSize"`
}

// NewSnapshot registers a new resource with the given unique name, arguments, and options.
func NewSnapshot(ctx *pulumi.Context,
	name string, args *SnapshotArgs, opts ...pulumi.ResourceOption) (*Snapshot, error) {
	if args == nil || args.VolumeId == nil {
		return nil, errors.New("missing required argument 'VolumeId'")
	}
	if args == nil {
		args = &SnapshotArgs{}
	}
	var resource Snapshot
	err := ctx.RegisterResource("aws:ebs/snapshot:Snapshot", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshot gets an existing Snapshot resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshot(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotState, opts ...pulumi.ResourceOption) (*Snapshot, error) {
	var resource Snapshot
	err := ctx.ReadResource("aws:ebs/snapshot:Snapshot", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Snapshot resources.
type snapshotState struct {
	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn *string `pulumi:"arn"`
	// The data encryption key identifier for the snapshot.
	DataEncryptionKeyId *string `pulumi:"dataEncryptionKeyId"`
	// A description of what the snapshot is.
	Description *string `pulumi:"description"`
	// Whether the snapshot is encrypted.
	Encrypted *bool `pulumi:"encrypted"`
	// The ARN for the KMS encryption key.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias *string `pulumi:"ownerAlias"`
	// The AWS account ID of the EBS snapshot owner.
	OwnerId *string `pulumi:"ownerId"`
	// A map of tags to assign to the snapshot
	Tags map[string]string `pulumi:"tags"`
	// The Volume ID of which to make a snapshot.
	VolumeId *string `pulumi:"volumeId"`
	// The size of the drive in GiBs.
	VolumeSize *int `pulumi:"volumeSize"`
}

type SnapshotState struct {
	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn pulumi.StringPtrInput
	// The data encryption key identifier for the snapshot.
	DataEncryptionKeyId pulumi.StringPtrInput
	// A description of what the snapshot is.
	Description pulumi.StringPtrInput
	// Whether the snapshot is encrypted.
	Encrypted pulumi.BoolPtrInput
	// The ARN for the KMS encryption key.
	KmsKeyId pulumi.StringPtrInput
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias pulumi.StringPtrInput
	// The AWS account ID of the EBS snapshot owner.
	OwnerId pulumi.StringPtrInput
	// A map of tags to assign to the snapshot
	Tags pulumi.StringMapInput
	// The Volume ID of which to make a snapshot.
	VolumeId pulumi.StringPtrInput
	// The size of the drive in GiBs.
	VolumeSize pulumi.IntPtrInput
}

func (SnapshotState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotState)(nil)).Elem()
}

type snapshotArgs struct {
	// A description of what the snapshot is.
	Description *string `pulumi:"description"`
	// A map of tags to assign to the snapshot
	Tags map[string]string `pulumi:"tags"`
	// The Volume ID of which to make a snapshot.
	VolumeId string `pulumi:"volumeId"`
}

// The set of arguments for constructing a Snapshot resource.
type SnapshotArgs struct {
	// A description of what the snapshot is.
	Description pulumi.StringPtrInput
	// A map of tags to assign to the snapshot
	Tags pulumi.StringMapInput
	// The Volume ID of which to make a snapshot.
	VolumeId pulumi.StringInput
}

func (SnapshotArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotArgs)(nil)).Elem()
}
